const express = require("express");
const app = express();
app.use(express.json());

// Sample data for Lowe's services/products
const lowesData = [
    { id: 1, service: 'Appliances', product: 'Cooktops', city: 'Arlington Heights', zipcode: '60005' },
    { id: 2, service: 'Bathroom', product: 'Bathroom Remodeling', city: 'Naperville', zipcode: '60564' },
    { id: 3, service: 'Exterior Home', product: 'Fencing', city: 'Northbrook', zipcode: '60062' },
    { id: 4, service: 'Flooring', product: 'Carpet', city: 'Carol Stream', zipcode: '60188' },
    { id: 5, service: 'Kitchen', product: 'Cabinets', city: 'Bolingbrook', zipcode: '60490' },
    { id: 6, service: 'Kitchen', product: 'Countertops', city: 'Northbrook', zipcode: '60062' },
    { id: 7, service: 'Exterior Home', product: 'Gutters', city: 'Bolingbrook', zipcode: '60490' },
    { id: 8, service: 'Bathroom', product: 'Sinks & Faucets', city: 'Northbrook', zipcode: '60062' },
    { id: 9, service: 'Appliances', product: 'Dishwashers', city: 'Arlington Heights', zipcode: '60005' },
    { id: 10, service: 'Flooring', product: 'Hardwood Flooring', city: 'Carol Stream', zipcode: '60188' },
    { id: 11, service: 'Bathroom', product: 'Toilets', city: 'Naperville', zipcode: '60564' },
    { id: 12, service: 'Kitchen', product: 'Garbage Disposals', city: 'Bolingbrook', zipcode: '60490' },
    { id: 13, service: 'Flooring', product: 'Tile Flooring', city: 'Naperville', zipcode: '60564' },
    { id: 14, service: 'Appliances', product: 'Refrigerators', city: 'Arlington Heights', zipcode: '60005' },
    { id: 15, service: 'Exterior Home', product: 'Roofing', city: 'Carol Stream', zipcode: '60088' }
];

// Home route
app.get("/", (req, res) => {
    res.send("Welcome to Lowe's Home Improvement API");
});

// GET endpoint to retrieve all services/products
app.get("/services", (req, res) => {
    res.json(lowesData);
});

// POST endpoint to add a new service/product
app.post("/services", (req, res) => {
    const { service, product, city, zipcode } = req.body;
    const id = lowesData.length + 1;
    const newService = { id, service, product, city, zipcode };
    lowesData.push(newService);
    res.status(201).json(newService);
});

// PUT endpoint to update an existing service/product
app.put("/services/:id", (req, res) => {
    const id = parseInt(req.params.id);
    const serviceToUpdate = lowesData.find(entry => entry.id === id);

    if (!serviceToUpdate) {
        return res.status(404).json({ error: "Service not found" });
    }

    const updatedData = req.body;
    Object.assign(serviceToUpdate, updatedData);
    res.json(serviceToUpdate);
});

// DELETE endpoint to delete a service/product
app.delete("/services/:id", (req, res) => {
    const id = parseInt(req.params.id);
    const index = lowesData.findIndex(entry => entry.id === id);

    if (index === -1) {
        return res.status(404).json({ error: "Service not found" });
    }

    lowesData.splice(index, 1);
    res.status(200).json({ message: "Service deleted" });
});

// Start the server
app.listen(3000, () => {
    console.log("Lowe's service running on http://localhost:3000");
});
