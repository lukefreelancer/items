

import React, { Component } from 'react';
import './App.css';


class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            items: [
                {
                    id: 1,
                    name: 'Kristina Zasiadko',
                    image:
                        'https://media.geeksforgeeks.org/wp-content/uploads/20230816223829/geeksgforgeeks-logo-1.png',
                },
                {
                    id: 2,
                    name: 'John Doe',
                    image:
'https://media.geeksforgeeks.org/wp-content/uploads/20230721212159/gfg-logo.jpeg',
                },
                {
                    id: 3,
                    name: 'Jane Smith',
                    image:
'https://media.geeksforgeeks.org/wp-content/uploads/20230909123918/GeeksforGeeks-Wide-logo-black.png',
                },
                // Add more items here
            ],
            draggingItem: null,
            newItemName: '',
            newItemImage: '',
        };
    }

    handleDragStart = (e, item) => {
        this.setState({ draggingItem: item });
        e.dataTransfer.setData('text/plain', '');
    };

    handleDragEnd = () => {
        this.setState({ draggingItem: null });
    };

    handleDragOver = (e) => {
        e.preventDefault();
    };

    handleDrop = (e, targetItem) => {
        const { draggingItem, items } = this.state;
        if (!draggingItem) return;

        const currentIndex = items.indexOf(draggingItem);
        const targetIndex = items.indexOf(targetItem);

        if (currentIndex !== -1 && targetIndex !== -1) {
            items.splice(currentIndex, 1);
            items.splice(targetIndex, 0, draggingItem);
            this.setState({ items });
        }
    };

    handleNameChange = (e) => {
        this.setState({ newItemName: e.target.value });
    };

    handleImageChange = (e) => {
        this.setState({ newItemImage: e.target.value });
    };

    addNewItem = () => {

        // Generate a unique ID for the new item
        const newItemId =
            Math.max(...this.state.items.map((item) => item.id)) + 1;
        const newItem = {
            id: newItemId,
            name: this.state.newItemName,
            image: this.state.newItemImage,
        };

        // Add the new item to the state
        this.setState({
            items: [...this.state.items, newItem],
            newItemName: '', // Clear the input fields
            newItemImage: '',
        });
    };

    render() {
        return (
            <div className="sortable-list">
                <div className="new-item">
                    <input
                        type="text"
                        placeholder="Name"
                        value={this.state.newItemName}
                        onChange={this.handleNameChange}
                        className="input-field"
                    />
                    <input
                        type="text"
                        placeholder="Image URL"
                        value={this.state.newItemImage}
                        onChange={this.handleImageChange}
                        className="input-field"
                    />
                    <button onClick={this.addNewItem}
                            className="add-button">
                        Add New Item
                    </button>
                </div>
                {this.state.items.map((item, index) => (
                    <div
                        key={item.id}
                        className=
                            {`item ${item === this.state.draggingItem ?
                                'dragging' : ''
                            }`}
                        draggable="true"
                        onDragStart={(e) =>
                            this.handleDragStart(e, item)}
                        onDragEnd={this.handleDragEnd}
                        onDragOver={this.handleDragOver}
                        onDrop={(e) => this.handleDrop(e, item)}
                    >
                        <div className="details">
                            <img src={item.image} alt={item.name} />
                            <span>{item.name}</span>
                        </div>

                        {/* Use the React icon component */}
                    </div>
                ))}
            </div>
        );
    }
}

export default App;
