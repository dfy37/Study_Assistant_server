const mathjax = require("mathjax-node"), yuml2svg = require('yuml2svg');

mathjax.start();

function convert(type, str, theme){
    if (type === 'yuml'){
        yuml2svg(str,{isDark:theme === 'dark'}).then(v => {
            console.log(v);
        }).catch(e => {
            console.log(false);
        });
    } else if(type === 'tex'){
        mathjax.typeset({
            math:str,
            format:'TeX',
            svg:true
        }, (data) => {
            if(theme === 'dark'){
                data.svg = data.svg.replace(/fill="currentColor"/g,'fill="#c0c0c0"');
            }else{
                data.svg = data.svg.replace(/fill="currentColor"/g,'fill="#515151"');
	    };
            console.log(data.svg)
        })
    } else {
        console.log(false);
    }
}

var args = process.argv.slice(2);
convert(args[0], args[1], args[2])

