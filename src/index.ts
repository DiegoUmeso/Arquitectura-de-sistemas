    import express = require("express");

    const app = express();

    app.use(express.json());

    let libros = [
        {
            id: 1,
            titulo: "Los tres cochinitos",
            autor: "Cuento tradicional",
            prestado: false
        },
        {
            id: 2,
            titulo: "Don Quijote",
            autor: "Miguel de Cervantes",
            prestado: true
        }
    ];

    app.get("/books", (req, res) => {
        res.json(libros);
    });

    app.post("/books", (req, res) => {

        if (!req.is("application/json")) {
            return res.status(400).json({
                mensaje: "Debe enviar datos en formato JSON"
            });
        }

        const nuevoLibro = {
            id: libros.length + 1,
            titulo: req.body.titulo,
            autor: req.body.autor,
            prestado: req.body.prestado || false
        };

        libros.push(nuevoLibro);

        res.status(201).json(nuevoLibro);
    });

    app.get("/health/fitness", (req, res) => {

        const totalLibros = libros.length;

        const librosPrestados = libros.filter(libro =>
            libro.prestado == true
        ).length;

        let porcentaje = 0;

        if (totalLibros > 0) {
            porcentaje = librosPrestados / totalLibros;
        }

        if (totalLibros > 100 || porcentaje >= 0.80) {

            return res.status(503).json({
                estado: "Degradacion de Calidad",
                totalLibros: totalLibros,
                librosPrestados: librosPrestados,
                porcentajePrestados: porcentaje * 100
            });
        }

        res.status(200).json({
            estado: "Healthy",
            totalLibros: totalLibros,
            librosPrestados: librosPrestados,
            porcentajePrestados: porcentaje * 100
        });

    });

    app.listen(3000, () => {
        console.log("Servidor iniciado en puerto 3000");
    });