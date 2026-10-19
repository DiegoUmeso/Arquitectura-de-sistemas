
import express from "express";
import { getWelcomeMessage } from "@repo/shared";

const app = express();
const port = 3001;

app.get("/", (_req, res) => {
  res.send(getWelcomeMessage("Backend"));
});

app.listen(port, () => {
  console.log(`API funcionando en http://localhost:${port}`);
});
