// открывается
openModal = document.getElementById('openModal')
let span = document.getElementsByClassName("close")[0]

openModal.addEventListener('click',function(){
    document.getElementById('modal').style.display='block'
})
// закрывается
span.addEventListener('click',function(){
    document.getElementById('modal').style.display='none'
})
// открывается бургер
openburger = document.getElementById('openburger')
openburger.addEventListener('click',function(){
    document.getElementById('burger').style.display='block'

})
// закртывается бургер
let spann = document.getElementsByClassName("closes")[0]
spann.addEventListener('click',function(){
    document.getElementById('burger').style.display='none'
})
// модель
openModali = document.getElementById('openModali')
let spannn = document.getElementsByClassName("close")[0]

openModali.addEventListener('click',function(){
    document.getElementById('modal').style.display='block'
})

openModali = document.getElementById('openModali')
openModali.addEventListener('click',function(){
    burger = document.getElementById('burger').style.display='none'
})

// vk
vk = document.getElementById('vk')
vk.addEventListener('click',function(){
    location.href = 'https://vk.com'
})
// inst
inst = document.getElementById('inst')
inst.addEventListener('click',function(){
    location.href = 'https://en.wikipedia.org/wiki/Instagram'
})
// telegram
telegram = document.getElementById('telegram')
telegram.addEventListener('click',function(){
    location.href = 'https://telegram.org/?ysclid=lbtn9ovf1751511071'
})

openModal = document.getElementById('openModal')
openModal.addEventListener('click',function(){
    document.getElementById('bl1').style.filter = 'blur(50px)'
})
span.addEventListener('click',function(){
    document.getElementById('bl1').style.filter = 'blur(0px)'
})

// blur
openModal.addEventListener('click',function(){
    document.getElementById('bl2').style.filter = 'blur(50px)'
})
span.addEventListener('click',function(){
    document.getElementById('bl2').style.filter = 'blur(0px)'
})
