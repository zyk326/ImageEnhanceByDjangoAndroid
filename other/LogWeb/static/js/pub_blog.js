window.onload = function (){
    const { createEditor, createToolbar } = window.wangEditor

    const editorConfig = {
        placeholder: 'Type here...',
        onChange(editor) {
            const html = editor.getHtml()
            console.log('editor content', html)
            // 也可以同步到 <textarea>
        }
    }

    const editor = createEditor({
        selector: '#editor-container',
        html: '<p><br></p>',
        config: editorConfig,
        mode: 'default', // or 'simple'
    })

    const toolbarConfig = {}

    const toolbar = createToolbar({
        editor,
        selector: '#toolbar-container',
        config: toolbarConfig,
        mode: 'default', // or 'simple'
    })

    $('#submit-btn').click(function (event){
        //组织按钮的默认行为
        event.preventDefault();

        let title = $("input[name='title']").val();
        let category = $('#category-select').val();
        let content = editor.getHtml();
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax('/blog/pub/', {
            method: 'POST',
            data: {title, category, content, csrfmiddlewaretoken},
            success: function (result){
                if(result['code']==200){
                    window.location = '/blog/detail/' + result['data']['blog_id']
                }else{
                    alert(result['message'])
                }
            }
        })
    })
}

