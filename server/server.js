const http = require('http');
const checkNewTrains = require('./functions/checkNewTrains');
const callAPI = require('./functions/callAPI')
const notifyUser = require('./functions/notifyUser');
const updateTrainsInTrip = require('./functions/updateTrainsInTrip');
const server = http.createServer((req, res) => {
    res.end('This is my server response!');
});

main = () => {
    while(true){
        getAllTripsFromDB().then((trips)=> {
            _.forEach(trips,(trip)=>{
                trains = callAPI(trip);
                new_trains = checkNewTrains(trip,trains);
                _.forEach(new_trains,(new_train)=>{
                    notifyUser(trip,new_train);
                    updateTrainsInTrip(trip,train);
                })
            })
        })
        sleep();
    }
}

main();

server.listen(process.env.PORT || 3000);


