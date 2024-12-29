// Import required modules
const express = require('express');
const multer = require('multer');
const path = require('path');

// Create an Express app
const app = express();
const port = 3000;

// Set up multer for file upload handling
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        // Set the path where images will be stored
        cb(null, path.join(__dirname, '../backend/static/uploads')); // Path to 'uploads' folder
    },
    filename: (req, file, cb) => {
        cb(null, Date.now() + path.extname(file.originalname)); // Use unique filenames
    }
});

const upload = multer({ storage: storage });

// Middleware to serve static files like images, CSS, JS, etc.
app.use(express.static(path.join(__dirname, '../frontend'))); // Serve static files from 'frontend' folder

// Parse incoming form data (for text input, etc.)
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Route to display the homepage
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../frontend', 'index.html')); // Serve the homepage from 'frontend'
});

// Route to upload a lost item image and details
app.post('/upload-lost-item', upload.single('lostImage'), (req, res) => {
    if (!req.file) {
        return res.status(400).send('No file uploaded.');
    }

    // Here you would typically save the file information and form data to your database
    const lostItem = {
        name: req.body.name,
        description: req.body.description,
        image: req.file.path, // Store file path
    };

    // Respond back with the uploaded file and item details (for testing)
    res.json({
        message: 'Lost item uploaded successfully!',
        item: lostItem
    });
});

// Route to serve the found items gallery page
app.get('/gallery', (req, res) => {
    res.sendFile(path.join(__dirname, '../frontend', 'gallery.html')); // Serve the gallery page from 'frontend'
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
