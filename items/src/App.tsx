import React, {useState, useRef} from 'react';
import logo from './logo.svg';
import './App.css';
import { available } from "./data";

function App() {
  const [data, setData] = useState(available);
  const [isDragging, setIsDragging] = useState(available);
  const containerRef = useRef();


  function dragStart(e, index){
    if (!detectLeftButton()) return;
    setIsDragging(index);

    const container = containerRef.current;
    console.log(container);
    const items = [...container.childNodes];
    const dragItem = items[index];

    const itemsBelowDragItem = items.slice(index + 1);
    const notDragItems = items.filter((_, i) => i !== index);
    const dragData = data[index];
    let newData = [...data];
    console.log(notDragItems);



    const dragBoundingRect = dragItem.getBoundingClientRect();
    // LEFT AT 20:11
    const space = items[1].getBoundingClientRect().top - items[0].getBoundingClientRect().bottom;
    console.log(space);

    dragItem.style.position = "fixed";
    dragItem.style.zIndex = 5000;
    dragItem.style.width = dragBoundingRect.width +"px";
    dragItem.style.height = dragBoundingRect.height + "px";
    dragItem.style.top = dragBoundingRect.top + "px";
    dragItem.style.left = dragBoundingRect.left + "px";
    dragItem.style.cursor = "grabbing";
    const div = document.createElement("div");
    div.id = "div-temp";
    div.style.width = dragBoundingRect.width +"px";
    div.style.height = dragBoundingRect.height +"px";
    div.style.pointerEvents = "none";
    container.appendChild(div);

    const distance = dragBoundingRect.height + space;

    itemsBelowDragItem.forEach(item => {
      item.style.transform=`translateY(${distance}px)`
    })

    let x = e.clientX;
    let y = e.clientY;


    document.onpointermove = dragMove;

    function dragMove(e){
      const posX = e.clientX - x;
      const posY = e.clientY - y;

      dragItem.style.transform = `translate(${posX}px , ${posY}px)`;
      notDragItems.forEach(item => {
        const rect1 = dragItem.getBoundingClientRect();
        const rect2 = item.getBoundingClientRect();
        let isOverlapping =
          rect1.y < rect2.y + (rect2.height / 2 ) && rect1.y + (rect1.height / 2 ) > rect2.y;
        if (isOverlapping){
          // Swap positionn card
          if (item.getAttribute("style")){
            item.style.transform = "";
            index++;
          } else {
            item.style.transform = `translateY(${distance}px)`
            index--;
          }
          // swap data
          newData = data.filter(item => item.id !== dragData.id);
          newData.splice(index, 0, dragData);
        }
      });
    }
    console.log(dragBoundingRect);

    document.onpointerup= dragEnd;
    function dragEnd(){
      document.onpointerup = "";
      document.onpointermove = "";

      setIsDragging(undefined);
      dragItem.style = "";
      container.removeChild(div);
      items.forEach(item => item.style = "");
      setData(newData);
    }
  }

  function detectLeftButton(e){
    e = e || window.event;
    if ("buttons" in e){
      return e.buttons === 1;
    }
    let button = e.which || e.button;
    return button === 1;
  }



  return (
    <div className="App">
    <div className="container" ref={containerRef}>
      {
        data.map((item, index) => (
          <div key={item.id} onPointerDown={e=> dragStart(e, index)}>
            <div className={`card ${ isDragging === index ? 'dragging' :''}` }>
              <div className="img-container">
                <img src="./card.svg" alt=""/>
              </div>
              <div className="box">
                <h3> {item.title}</h3>
                <h4> {item.subtitle}</h4>
              </div>
            </div>
          </div>
        ))
      }
    </div>
    </div>
  );
}

export default App;
