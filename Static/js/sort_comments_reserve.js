var list = document.getElementById('commentList');
var items = list.childNodes;
var itemsArr = [];

for (var i in items) {

    if (items[i].nodeType == 1) { // get rid of the whitespace text nodes
        itemsArr.push(items[i]);
    }
}

console.log(itemsArr);

itemsArr.sort(function(a, b) {
    return a.id == b.id ? 0 : (a.id > b.id ? 1 : -1);
});

for (i = 0; i < itemsArr.length; ++i) {
    list.appendChild(itemsArr[i]);
}

