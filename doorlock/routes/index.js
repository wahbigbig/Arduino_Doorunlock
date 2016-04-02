var express = require('express');
var router = express.Router();
var fs = require('fs');

router.get('/unlock', function(req, res, next) {
	fs.writeFile('status.txt', '1', function(err) {
		if (err) {
			res.send('error writing the file');
		} else {
			res.send('1');
		}
	})  
});

router.get('/lock', function(req, res, next) {
	fs.writeFile('status.txt', '0', function(err) {
		if (err) {
			res.send('error writing the file');
		} else {
			res.send('0');
		}
	}) 
});

router.get('/status', function(req, res, next) {
	fs.readFile('status.txt', 'utf8', function(err, data) {
		if (err) {
			res.send('error reading the file');
		} else {
			res.send(data);
		}		
	});
});

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

module.exports = router;
