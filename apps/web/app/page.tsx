import { getWelcomeMessage } from "@repo/shared";

export default function Home() {
  const message = getWelcomeMessage("Frontend");

  return (
    <main
      style={{
        fontFamily: "Arial, sans-serif",
        padding: "40px",
        textAlign: "center",
      }}
    >
      <h1>Mi Frontend - Monorepo HW05</h1>

      <p>{message}</p>

      <p>Esta aplicacion utiliza la libreria compartida.</p>
    </main>
  );
}
