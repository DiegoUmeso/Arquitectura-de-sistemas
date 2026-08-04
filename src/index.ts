import express from "express";

const app = express();
const puerto = 3000;

app.use(express.json());

let pokemones = [
    {
        id: 1,
        nombre: "Pikachu",
        tipo: "Eléctrico",
        nivel: 25
    },
    {
        id: 2,
        nombre: "Charmander",
        tipo: "Fuego",
        nivel: 18
    }
];

// Ruta principal
app.get("/", (req, res) => {
    res.send("API de Pokemones funcionando correctamente");
});

// GET
app.get("/pokemones", (req, res) => {
    res.json(pokemones);
});

// POST
app.post("/pokemones", (req, res) => {

    const nuevo = {
        id: pokemones.length + 1,
        ...req.body
    };

    pokemones.push(nuevo);

    res.status(201).json(nuevo);

});

// PUT
app.put("/pokemones/:id", (req, res) => {

    const id = Number(req.params.id);

    const indice = pokemones.findIndex(p => p.id === id);

    if (indice === -1) {
        return res.status(404).json({
            mensaje: "Pokémon no encontrado"
        });
    }

    pokemones[indice] = {
        id,
        ...req.body
    };

    res.json(pokemones[indice]);

});

// PATCH
app.patch("/pokemones/:id", (req, res) => {

    const id = Number(req.params.id);

    const pokemon = pokemones.find(p => p.id === id);

    if (!pokemon) {
        return res.status(404).json({
            mensaje: "Pokémon no encontrado"
        });
    }

    Object.assign(pokemon, req.body);

    res.json(pokemon);

});

// DELETE
app.delete("/pokemones/:id", (req, res) => {

    const id = Number(req.params.id);

    pokemones = pokemones.filter(p => p.id !== id);

    res.json({
        mensaje: "Pokémon eliminado correctamente"
    });

});

// Iniciar servidor
app.listen(puerto, () => {
    console.log(`Servidor ejecutándose en http://localhost:${puerto}`);
});