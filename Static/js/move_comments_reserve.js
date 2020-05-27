var list = document.getElementById('commentList');
var items = list.childNodes;
var itemsArr = [];

for (var i in items) {

    if (items[i].nodeType == 1) { // get rid of the whitespace text nodes
        itemsArr.push(items[i]);
    }
}


itemsArr.forEach(item =>

    console.log(item.attributes.id.nodeValue)

    );
