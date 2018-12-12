const path = require("path");

module.exports = {
  outputDir: path.resolve(__dirname, "../server/static"),
  // Note: paths below are relative to `outputDir`.
  assetsDir: "./",
  indexPath: "../templates/index.html",
  devServer: {
    host: 'localhost',
    port: 5050,
    https: false
  }
}
