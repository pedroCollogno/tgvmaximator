const router = require('express').Router();

router.get("/runScripts", function(req,res){
    var PythonShell = require('python-shell');
    var pyshell = new PythonShell('../scripts/run_scripts.py');
    pyshell.end(function (err,code,signal) {
        if (err) throw err;
        console.log('finished');
        res.send('finished');
      });
});



module.exports = {router:router};