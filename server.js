const express = require('express');
const bodyParser = require('body-parser');
const multer = require('multer');
const { PythonShell } = require('python-shell');
const fs = require('fs');

const app = express();
const port = process.env.PORT || 3000;
const upload = multer({
  limits: {
    fileSize: 100 * 1024 * 1024,
  },
  'dest': './upload',
});

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.use(express.static('public'));

app.post('/blur', upload.single('qrcode'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('File missing!');
  }

  const options = {
    mode: 'text',
    pythonOptions: ['-u'], // get print results in real-time
    args: ['-i', `upload/${req.file.filename}`, '-o', `upload/${req.file.filename}.new.jpg`] //An argument which can be accessed in the script using sys.argv[1]
  };

  PythonShell.run('./main.py', options, async function (err, result){
    if (err) {
      console.error(err);
      res.status(500).send('Unknown server error');
      return;
    }
    if (result && result[0] === 'No QR code found') {
      res.header('Content-Type', 'image/jpeg').sendFile(`${__dirname}/upload/${req.file.filename}`, () => {
        fs.unlink(`${__dirname}/upload/${req.file.filename}`, (err => {
          if (err) console.error(err);
        }));
      });
    } else {
      res.sendFile(`${__dirname}/upload/${req.file.filename}.new.jpg`, () => {
        fs.unlink(`${__dirname}/upload/${req.file.filename}.new.jpg`, (err => {
          if (err) console.error(err);
        }))
        fs.unlink(`${__dirname}/upload/${req.file.filename}`, (err => {
          if (err) console.error(err);
        }));
      });
    }
    
  });
});

app.listen(port, function () {
  console.log('Server is running on PORT',port);
});