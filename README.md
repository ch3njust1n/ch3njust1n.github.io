## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


###
If getting the issue below, execute the following command in the frontend folder `./node_modules/.bin/eslint --init`
```
Module build failed (from ./node_modules/eslint-loader/index.js):
Error: No ESLint configuration found
```

###  https://github.com/vuejs/eslint-plugin-vue/issues/204
```
Parsing error: Unexpected token import
```

Add to `.eslintrc.json`:
```
"parserOptions": {
        "parser": "babel-eslint",...}
```