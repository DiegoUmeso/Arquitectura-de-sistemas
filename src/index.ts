import express from "express";
import swaggerUi from "swagger-ui-express";
import swaggerJsdoc from "swagger-jsdoc";

const app = express();
const puerto = 3000;

app.use(express.json());

const opciones = {
  definition: {
    openapi: "3.0.0",
    info: {
      title: "API de Pokémon",
      version: "1.0.0",
      description: "Documentación de la API de Pokémon"
    }
  },
  apis: ["./src/index.ts"]
};

const specs = swaggerJsdoc(opciones);

app.use("/docs", swaggerUi.serve, swaggerUi.setup(specs));

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

/**
 * @swagger
 * /pokemones:
 *   get:
 *     summary: Obtener todos los pokemones
 *     responses:
 *       200:
 *         description: Lista de pokemones
 */
app.get("/pokemones", (req, res) => {
  res.json(pokemones);
});

/**
 * @swagger
 * /pokemones:
 *   post:
 *     summary: Agregar un pokemon
 *     responses:
 *       201:
 *         description: Pokemon creado
 */
app.post("/pokemones", (req, res) => {
  const nuevo = {
    id: pokemones.length + 1,
    ...req.body
  };

  pokemones.push(nuevo);

  res.status(201).json(nuevo);
});

/**
 * @swagger
 * /pokemones/{id}:
 *   put:
 *     summary: Actualizar un pokemon completo
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *     responses:
 *       200:
 *         description: Pokemon actualizado
 */
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

/**
 * @swagger
 * /pokemones/{id}:
 *   patch:
 *     summary: Modificar parcialmente un pokemon
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *     responses:
 *       200:
 *         description: Pokemon modificado
 */
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

/**
 * @swagger
 * /pokemones/{id}:
 *   delete:
 *     summary: Eliminar un pokemon
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *     responses:
 *       200:
 *         description: Pokemon eliminado
 */
app.delete("/pokemones/:id", (req, res) => {

  const id = Number(req.params.id);

  pokemones = pokemones.filter(p => p.id !== id);

  res.json({
    mensaje: "Pokémon eliminado correctamente"
  });

});

app.listen(puerto, () => {
  console.log(`Servidor ejecutándose en http://localhost:${puerto}`);
});