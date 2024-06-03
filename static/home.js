color = ['#CCCCFF' , '#9999FF', '#6666FF', '#3333FF', '#0000FF', '#0000CC', '#000099', '#000066', '#000033', '#000000']

dog = (value)=>{
    value = Math.round(value/10)
    const dog = document.querySelectorAll('.dogdiv')
    for(let i = 0; i < value; i++){
        dog[i].style.backgroundColor = color[i];
    }
}


cat = (value)=>{
    value = Math.round(value/10)
    const cat = document.querySelectorAll('.catdiv')
    for(let i = 0; i < value; i++){
        cat[i].style.backgroundColor = color[i];
    }
}