let tags = document.getElementsByClassName("project-tag") // query the tags

for (let i = 0; tags.length > i; i++){
    tags[i].addEventListener('click', (e)=>{
        let tagId = e.target.dataset.tag
        let projectId = e.target.dataset.project

        fetch ('http://127.0.0.1:8000/api/remove-tag/', {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'project':projectId, 'tag':tagId})
        })
            .then(response => response.json())
            .then(data => {
                e.target.remove()
            })
    })
}