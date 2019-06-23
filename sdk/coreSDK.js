const app = require('./src/main');
let token = JSON.stringify('token');
const useToken = (req, token) => {
  req.token = token;
  app.use(req.token);
};
