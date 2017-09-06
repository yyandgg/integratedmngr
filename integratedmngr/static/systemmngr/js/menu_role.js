var MenuRoleRelation = function(){
    var initContents = function() {

        $("#form-field-select-1").change(function() {
            $("#role-tree").load('/systemmngr/get-tree-by-role-req/' + $(this).val() + "/");
        });
        $("#form-field-select-1").change();
    }
    
    return {
        init: function(){
            initContents();
        },
    };
}();
