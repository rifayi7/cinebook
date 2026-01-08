import React, {
  useEffect,
  useState,
  type HTMLInputTypeAttribute,
  type InputHTMLAttributes,
  type ReactElement,
} from "react";
import { useParams } from "react-router-dom";
import type { UserType } from "../../types/UsersType";

export default function SingleUserForAdmin() {
  const [user, setUser] = useState<UserType | null>(null);
  const [formData, setFormData] = useState<Partial<UserType | null>>(null);
  const [error, setError] = useState(null);
  const { id } = useParams<{ id: string }>();
  const fetchUser = async () => {
    try {
      const res = await fetch(`http://127.0.0.1:8000/api/admin/user/${id}`);
      if (!res.ok) {
        throw new Error("failed to fetch from api");
      }
      const data = await res.json();
      setFormData(data);
    } catch (error: any) {
      setError(error);
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === "checkbox" ? checked : value,
    });
  };

  const handleSaveChange = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const res = await fetch(`http://127.0.0.1:8000/api/admin/user/${id}`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });
      if (!res.ok) {
        throw new Error("something went wrong while updating the user details");
      }
      const data = res.json();
      console.log(data);
    } catch (error: any) {
      setError(error);
    }
  };

  useEffect(() => {
    fetchUser();
  }, []);
  if (!formData) return <div>User not found</div>;
  return (
    <div className="w-full min-h-screen bg-gray-100 p-5">
      <form
        onSubmit={handleSaveChange}
        className="bg-white p-4 w-fit rounded shadow-[0px_2px_3px_-1px_rgba(0,0,0,0.1),0px_1px_0px_0px_rgba(25,28,33,0.02),0px_0px_0px_1px_rgba(25,28,33,0.08)]"
      >
        <table>
          <tbody>
            <Input
              name="id"
              type="number"
              label="id"
              readOnly
              value={formData?.id}
              onChange={handleChange}
            />
            <Input
              name="username"
              type="text"
              label="username"
              value={formData?.username}
              onChange={handleChange}
            />
            <Input
              name="email"
              type="email"
              label="email"
              value={formData?.email}
              onChange={handleChange}
            />
            <CheckBox
              label="is_active"
              checked={formData?.is_active}
              onChange={handleChange}
              name="is_active"
            />
            <CheckBox
              label="is_staff"
              checked={formData?.is_staff}
              onChange={handleChange}
              name="is_staff"
            />
          </tbody>
        </table>
        <button type="submit" className="bg-blue-600">
          Submit
        </button>
      </form>
    </div>
  );
}

function Input({
  label,
  ...props
}: { label: string } & React.InputHTMLAttributes<HTMLInputElement>) {
  return (
    <tr>
      <td className="p-2">{label}</td>
      <td>
        <input {...props} className="w-full  rounded px-3 py-2" />
      </td>
    </tr>
  );
}

function CheckBox({
  label,
  ...props
}: { label: string } & React.InputHTMLAttributes<HTMLInputElement>) {
  return (
    <tr>
      <td className="p-2">
        <label htmlFor={label}>
          <input type="checkbox" id={label} {...props} />
          {label}
        </label>
      </td>
    </tr>
  );
}
