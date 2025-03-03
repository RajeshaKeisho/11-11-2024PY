import React, { useState, useEffect } from 'react';

function App() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/items/')
      .then(response => response.json())
      .then(data => {
        console.log('Fetched data:', data);
        setItems(data.items);
      })
      .catch(error => console.error('Error fetching data:', error));
  }, []);
  
  return (
    <div style={styles.container}>
      <h1 style={styles.header}>Items</h1>
      <div style={styles.gridContainer}>
        {items.map(item => (
          <div key={item.id} style={styles.gridItem}>
            <strong>{item.name}</strong>
            <p>{item.description}</p>
            <p>Availability: {item.is_available ? 'Yes' : 'No'}</p>
            <p>Price: Rs. {item.price}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

// Define inline styles
const styles = {
  container: {
    textAlign: 'center',
    margin: '20px',
  },
  header: {
    fontSize: '24px',
    fontWeight: 'bold',
    marginBottom: '10px',
  },
  gridContainer: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
  },
  gridItem: {
    width: '300px',
    background: '#eee',
    margin: '10px',
    padding: '15px',
    borderRadius: '5px',
  },
};

export default App;
