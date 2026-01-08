import { BrowserRouter, Route, Routes } from "react-router-dom";
import AdminDashBoard from "./pages/Admin/AdminDashBoard";
import SingleUserForAdmin from "./pages/Admin/SingleUserForAdmin";
import IndexPage from "./pages/IndexPage";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="admin/users" element={<AdminDashBoard />} />
          <Route path="admin/user/:id" element={<SingleUserForAdmin />} />
          <Route path="/" element={<IndexPage />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
