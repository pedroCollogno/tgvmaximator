const account = require('./auth/lib.js');
const Trip = require('../schema/Trip');

module.exports = function (app) {
    app.get('/',account.isAuth, (req, res, next) => {
        console.log("Accessing trip info");
        Trip.find({}, function(err, trips) {
            return res.status(200).json(trips);
        })
    });
}