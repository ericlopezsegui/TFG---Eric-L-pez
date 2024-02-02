const express = require('express');
const app = express();

const routes = [
    './routes/torneigRoutes',
    './routes/adminRoutes',
    './routes/arbitRoutes',
    './routes/campRoutes',
    './routes/classificacioRoutes',
    './routes/equipRoutes',
    './routes/golRoutes',
    './routes/grupRoutes',
    './routes/jugadorRoutes',
    './routes/partitRoutes',
    './routes/personalRoutes',
    './routes/sancionsRoutes',
    './routes/ubicacioRoutes'
];


app.use(express.json());
app.use(express.urlencoded({ extended: true }));

routes.forEach(route => {
    app.use(require(route));
});

app.listen(process.env.PORT, () => {
    console.log('Server is running on port 3000');
});