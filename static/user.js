function pdf(nodeId) {
    family.exportPDF({
         format: "A4"
    });
 }

var family = new FamilyTree(document.getElementById('tree'), {
    mouseScrool: FamilyTree.action.scroll,
    showYScroll: FamilyTree.scroll.visible,
    showXScroll: FamilyTree.scroll.visible,
    scaleInitial: FamilyTree.match.boundary,
    mode: 'light',
    template: 'hugo',
    nodeMenu: {
        details: { text: 'Details' },
    },
    
    nodeBinding: {
        field_0: 'name',
        field_1: 'born',
        img_0: 'photo'
    },
    editForm: {
        titleBinding: "name",
        photoBinding: "photo",
        

        generateElementsFromFields: true,
        elements: [
            { type: 'textbox', label: 'Full Name', binding: 'name' },
            { type: 'textbox', label: 'Email Address', binding: 'email' },
            [
                { type: 'textbox', label: 'Phone', binding: 'phone' },
                { type: 'date', label: 'Date Of Birth', binding: 'born' }
            ],
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

button.addEventListener("click", function() {
    alert("Proses Penyimpanan");
    pdf();
  });
family.load(data)


FamilyTree.scroll.safari = {smooth: 12,speed: 500};
FamilyTree.scroll.ie = { smooth: 12, speed: 200 };
FamilyTree.scroll.edge = { smooth: 12, speed: 200 };
FamilyTree.scroll.chrome = { smooth: 12, speed: 200 };
FamilyTree.scroll.firefox = { smooth: 12, speed: 200 };
FamilyTree.scroll.opera = { smooth: 12, speed: 200 };