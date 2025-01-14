
const input = document.querySelector('.input'); //selecting the first element with class input
// getting the tags and inpiut elements from the DOM

// creating a container for the tags
const tagsContainer = document.createElement('ul');
tagsContainer.classList.add('tags');
input.parentElement.insertBefore(tagsContainer, input); // Add the <ul> before the textarea


// adding an event litsener for keydown on input element
input.addEventListener('keydown', function (event) {
    //check if key pressed is enter
    if (event.key === 'Enter'){
        event.preventDefault(); //prevent the default action of keypress

        
        // get the trimmed value of the input element
        const tagContent = input.Value.trim();
        // check if trimmed value is not an empty string
        if(tagContent !== ''){

            const existingTags = Array.from(tagsContainer.children).map(tag=>
                tag.firstChild.textContent.trim() // getting the textcontent of each tag
            );

            if (existingTags.includes(tagContent)){
                const tag = document.createElement('li'); //create a new list item element for the tag
                tag.classList.add('tag');
                tag.innerText = t
                
                // Adding a delete button to the tag
                const deleteButton = document.createElement('button');
                deleteButton.innerTex = 'X';
                deleteButton.classList.add('dele-button');
                tag.appendChild(deleteButton);

                tagsContainer.appendChild(tag); // append the tag to the tags list
                
                input.value = ''; //clear the inputs elements

            } else {
                alert('Tag already exists!'); //alert user if tag already exists
            }
            
        }
    }
});

// Add an event-listener for clicking on the tag list

tags.addEventListener('click', function(event){
    if (event.target.classList.contains('delete-button')){  //check if the clicked element has the class 'delete-button'
        event.target.parentElement.remove(); //remove the parent element (the tag)

    }
});