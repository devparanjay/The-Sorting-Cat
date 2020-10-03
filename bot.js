import {  } from "discord.js";

// eslint-disable-next-line no-undef
Discord = require('discord.js');
// eslint-disable-next-line no-undef
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content === 'ping') {
    msg.reply('Pong!');
  }
});

// eslint-disable-next-line no-undef
client.login(process.env.BOT_TOKEN);