let balance = 0

function watchAd(){
balance += 5
document.getElementById("bal").innerText = balance
alert("Ad watched +5 Tk")
}

function show(page){

let pages = ["home","ref","wallet","account","leader"]

pages.forEach(p=>{
document.getElementById(p).style.display="none"
})

document.getElementById(page).style.display="block"

}
