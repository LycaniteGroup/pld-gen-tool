const htmlPdf = require('html-pdf-chrome');
const options = {
        host: 'chrome',
        port: 7575, // port Chrome is listening on
        printOptions: {
            printBackground: true,
            marginLeft: 0,
            marginRight: 0,
            marginTop: 0,
            marginBottom: 0,
            preferCSSPageSize: true
        }
    };
const url = process.env['SITE_URL'] || 'http://localhost:8000';

(async () => {
    const pdf = await htmlPdf.create(url, options);
    const date = new Date();
    const now = `${date.getDay()}-${date.getMonth()}-${date.getFullYear()}`;
    const name = `${process.env['BUILD_NAME'] || now}`
    const buildPath = `${process.env['BUILD_PATH'] || '../build'}`
    await pdf.toFile(`${buildPath}/${name}.pdf`)
    console.log(`Finished building ${name}.pdf`);
})();
