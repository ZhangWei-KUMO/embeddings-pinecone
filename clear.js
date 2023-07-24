import * as fs from 'fs';
var filepath = './files.txt'

var data = fs.readFileSync(filepath, 'utf-8');
const trimmedStr = data.replace(/\n|\r/g,"").replace(/\s+/g, '')
fs.writeFileSync(filepath, trimmedStr, 'utf-8');