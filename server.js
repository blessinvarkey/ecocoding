var express = require('express'),
    mds = require('markdown-serve'),
    path = require('path');

var app = express();

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(mds.middleware({
    rootDirectory: path.resolve(__dirname, '/'),
    view: 'markdown'
}));
