import { useEffect, useState } from "react";
import type { UserType } from "../../types/UsersType";

export default function AdminDashBoard() {
  const [userList, setUserList] = useState<UserType[]>([]);
  const [error, setError] = useState<any>(null);
  const fetchUsers = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/api/admin/users");
      if (!res.ok) {
        throw new Error("failed to fetch from api");
      }
      const data = await res.json();
      setUserList(data);
    } catch (error: any) {
      console.log(error);
      setError(error);
    }
  };
  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <div className="w-full min-h-screen bg-gray-100 p-6">
      {error && <h1 className="text-red-50">{error?.message}</h1>}
      <h1 className="text-2xl font-semibold text-gray-800 mb-6">Users</h1>

      <div className="bg-white rounded-lg shadow overflow-hidden">
        <table className="w-full text-sm">
          <thead className="bg-gray-50 border-b">
            <tr className="text-left text-gray-600">
              <th className="px-4 py-3">Username</th>
              <th className="px-4 py-3">Email</th>
              <th className="px-4 py-3">Status</th>
              <th className="px-4 py-3">Role</th>
            </tr>
          </thead>

          <tbody>
            {userList?.map((user) => (
              <tr
                key={user.id}
                className="border-b hover:bg-gray-50 cursor-pointer"
              >
                <td className="px-4 py-3 font-medium text-gray-800">
                  {user.username}
                </td>

                <td className="px-4 py-3 text-gray-600">{user.email}</td>

                <td className="px-4 py-3">
                  <span
                    className={`px-2 py-1 rounded text-xs ${
                      user.is_active
                        ? "bg-green-100 text-green-700"
                        : "bg-red-100 text-red-700"
                    }`}
                  >
                    {user.is_active ? "Active" : "Inactive"}
                  </span>
                </td>

                <td className="px-4 py-3 text-gray-600">
                  {user.is_admin ? "Admin" : user.is_staff ? "Staff" : "User"}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
