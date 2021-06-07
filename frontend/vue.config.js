module.exports = {
  outputDir: "../app/static",
  productionSourceMap: false,

  devServer: {
    proxy: {
      "^/api": {
        target: "http://localhost:5000",
        changeOrigin: true,
        logLevel: "debug",
        pathRewrite: { "^/api": "/api" }
      },
      "^/storage": {
        target: "http://localhost:5000",
        changeOrigin: true,
        logLevel: "debug",
        pathRewrite: { "^/storage": "/storage" }
      }
    }
  },

  publicPath: process.env.NODE_ENV === "production" ? "/" : "/"
}
