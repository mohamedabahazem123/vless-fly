import { WebSocketServer } from 'ws';
import { createServer } from 'http';
const UUID = '53f3e66a-4d03-4c55-9b41-6aeee4c0a0e2';
const PATH = '/Telegram/@MarocProxy/@Server1';
const server = createServer();
const wss = new WebSocketServer({ server, path: PATH });
wss.on('connection', (ws) => { console.log('Client connected'); });
server.listen(process.env.PORT || 8080);
console.log(`Server running on port ${process.env.PORT || 8080}`);
