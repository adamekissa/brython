from browser import document, html, alert, console

      counter = 1

      def showtext(e):
          global someGlobal
          someGlobal = e.target.value


      def createTask(e):
          global counter
          console.log(counter)
          
         
          element = document['justadiv']
          x = document['input'].value
          if x == "":
            return
          
          newButton = html.BUTTON("Delete Task", Id="delete-task")
          counter += 1
          console.log(counter)
          newDiv = html.DIV(Id=counter)
          newP = html.P(someGlobal)
          newP.classList.add("bg-white", "rounded")
          newDiv <= newP
          newDiv <= newButton
          element <= newDiv
          document['input'].value=""

      def delete():
          console.log("I was clicked")


      
     
      document['add-task'].bind("click", createTask)
      document['input'].bind('input', showtext)
      document['delete-task'].bind("click", delete)