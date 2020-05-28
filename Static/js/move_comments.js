var list = document.getElementById('commentList');
var items = list.childNodes;
var itemsArr = [];
var idArr = [];

for (var i in items) {

    if (items[i].nodeType == 1) { // get rid of the whitespace text nodes
        itemsArr.push(items[i]);
    }
}


let commentId = ""
itemsArr.forEach(item =>
    (idArr.push(item.attributes.id.nodeValue))
    );


for (i = 0; i < idArr.length; ++i) {
    let indent = 10
    let column_width = 5
    console.log(document.getElementById(idArr[i]));
    let column = ((idArr[i].match(/-/g)||[]).length);
    document.getElementById(idArr[i]).style.marginLeft = (column*column_width*indent)+"px"

}

let commentSpace = document.querySelector('.comments-space');
commentSpace.classList.remove('hide');