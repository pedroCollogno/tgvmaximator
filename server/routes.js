const router = require('express').Router();

router.get('/', function(req, res){
    res.send('Hello');
});

router.get('/runScripts', function(req, res){
    var PythonShell = require('python-shell').PythonShell;
    var pyshell = new PythonShell('../scripts/run_scripts.py');
    console.log('Starting running scripts...');
    pyshell.end(function (err, code, signal) {
        if (err) throw err;
        console.log('Finished!');
        res.send('finished');
      });
});



module.exports = {router:router};