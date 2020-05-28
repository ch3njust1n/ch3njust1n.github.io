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

Todo:
1. Responsive nav bar
2. Breakpoints for sect 1
3. Make mobile friendly
4. About information on 501(c)(3) mission
5. About directors
6. Current conference sponsors
7. Conference information
8. Hover nav items fade color
9. Information on joining us and that we're looking for talent researchers
	- make sure to add info that this is not a paid position and inquire for more information
10. Add pictures from conferences
11. Information on current conference
12. On scroll, after scroll down P px, switch menu to pancake icon
13. Twitter feed with just text no embedding
