function pdf(nodeId) {
    family.exportPDF({
         format: "A4"
    });
 }
console.log(data)
var family = new FamilyTree(document.getElementById('tree'), {
    mouseScrool: FamilyTree.action.scroll,
    showYScroll: FamilyTree.scroll.visible,
    showXScroll: FamilyTree.scroll.visible,
    scaleInitial: FamilyTree.match.boundary,
    menu: {
        export_pdf: {
            text: "Export PDF",
            icon: FamilyTree.icon.pdf(24, 24, "#7A7A7A"),
            onClick: pdf
        },
        xml: { text: "Export XML" },
        csv: { text: "Export CSV" },
        json: { text: "Export JSON" },
        importJSON: {text: "Import JSON", icon: FamilyTree.icon.json(24,24,'red'), onClick: importJSONHandler},
        importXML: {text: "Import XML", icon: FamilyTree.icon.xml(24,24,'red'), onClick: importXMLHandler},
        importCSV: {text: "Import CSV", icon: FamilyTree.icon.csv(24,24,'red'), onClick: importCSVHandler}
    },
    mode: 'light',
    template: 'hugo',
    nodeMenu: {
        edit: { text: 'Edit' },
        details: { text: 'Details' },
    },
    nodeTreeMenu: true,
    nodeBinding: {
        field_0: 'name',
        field_1: 'born',
        field_2: 'death',
        img_0: 'photo'
    },
    editForm: {
        titleBinding: "name",
        photoBinding: "photo",
        addMoreBtn: 'Add element',
        addMore: 'Add more elements',
        addMoreFieldName: 'Element name',
        generateElementsFromFields: false,
        elements: [
            { type: 'textbox', label: 'Full Name', binding: 'name' },
            [
                { type: 'textbox', label: 'Email Address', binding: 'email' },
                { type: 'textbox', label: 'Phone', binding: 'phone' },
                
            ],
            { type: 'date', label: 'Birth Date', binding: 'born' },
            { type: 'date', label: 'Death Date', binding: 'death' },
            [
                { type: 'select', options: [{ value: 'bg', text: 'Bulgaria' }, { value: 'ru', text: 'Russia' }, { value: 'gr', text: 'Greece' }], label: 'Country', binding: 'country' },
                { type: 'textbox', label: 'City', binding: 'city' },
            ],
            { type: 'textbox', label: 'Photo Url', binding: 'photo', btn: 'Upload' },
        ]
    },
});

family.on('field', function (sender, args) {
    if (args.name == 'born') {
        var date = new Date(args.value);
        args.value = date.toLocaleDateString();
    }
});

function importJSONHandler(){
    family.importJSON();
}
function importXMLHandler(){
    family.importXML();
}

function importCSVHandler(){
    family.importCSV();
}

button.addEventListener("click", function() {
    alert("Proses Penyimpanan");
    pdf();
  });
// var data = JSON.parse('{{ data|safe }}');
family.load(data)
FamilyTree.scroll.safari = {smooth: 12,speed: 500};
FamilyTree.scroll.ie = { smooth: 12, speed: 200 };
FamilyTree.scroll.edge = { smooth: 12, speed: 200 };
FamilyTree.scroll.chrome = { smooth: 12, speed: 200 };
FamilyTree.scroll.firefox = { smooth: 12, speed: 200 };
FamilyTree.scroll.opera = { smooth: 12, speed: 200 };