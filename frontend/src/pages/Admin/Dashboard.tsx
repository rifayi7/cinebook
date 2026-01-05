import { useEffect } from "react";

export default function Dashboard() {
  // useEffect(() => {
  //   const dataFetch = async () => {
  //     const res = await fetch("http://127.0.0.1:8000/api/");
  //     const data = await res.json();
  //     console.log(data);
  //   };

  //   dataFetch();
  // });

  const formSubmit = async (e: any) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const email = formData.get("email");
    const password = formData.get("password");
    const username = formData.get("username");
    console.log(email, password, username);
    try {
      const res = await fetch("http://127.0.0.1:8000/api/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password, email, is_staff: true }),
      });
      const data = await res.json();
      console.log(data);
    } catch (err) {
      console.log(err);
    }
  };
  return (
    <div>
      <h1>Admin Dashboard</h1>
      <p>Welcome to the admin dashboard</p>
      <form
        onSubmit={formSubmit}
        style={{
          display: "flex",
          flexDirection: "column",
          width: "30%",
          gap: "20px",
        }}
      >
        <input type="text" name="username" placeholder="Username" />
        <input type="password" name="password" placeholder="Password" />
        <input type="email" name="email" placeholder="Email" />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}
