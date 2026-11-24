const { copyFileSync } = require('node:fs');
const { join } = require('node:path');

copyFileSync(join(__dirname, 'entry.png'), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));
