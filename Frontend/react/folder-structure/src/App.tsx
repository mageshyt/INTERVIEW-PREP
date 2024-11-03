import { useState } from 'react';
import './App.css'



interface FolderNode {
  id: string;
  name: string;
  children: FolderNode[];
  type: "FOLDER" | "FILE";
  parentId: string | null;
}

import { FcOpenedFolder, FcFolder, FcFile, FcAddRow, FcPlus } from "react-icons/fc";
import { FiTrash } from 'react-icons/fi';
function App() {
  const [parent, setParent] = useState<FolderNode>({
    id: '46598644-304e-4f44-9c01-f903faf319e0',
    parent: null,
    name: 'Folder 1',
    type: "FOLDER",
    children: []
  })

  const findNode = (id: string, node: FolderNode): FolderNode => {
    if (node.id === id) {
      return node
    }

    for (const child of node.children) {
      const found = findNode(id, child)
      if (found) return found
    }

    return null

  }
  const createAsset = (name: string, parentId: string | null, type: "FOLDER" | "FILE") => {
    const newAsset: FolderNode = {
      id: crypto.randomUUID(),
      name,
      type,
      parentId,
      children: []
    };

    if (parentId) {
      const nodeParent = findNode(parentId, parent);
      if (!nodeParent) {
        console.error(`Parent with ID ${parentId} not found`);
        return;
      }

      nodeParent.children.push(newAsset);
      setParent(prevParent => ({ ...prevParent }));
    }

    return newAsset;
  }

  const deleteAsset = (id: string) => {

    const currenNode = findNode(id, parent)
    if (!currenNode || !currenNode.parentId) return
    const nodeParent = findNode(currenNode?.parentId, parent)
    console.log(nodeParent)

    nodeParent.children = nodeParent.children.filter(child => child.id !== id)

    setParent(prevParent => ({ ...prevParent }))
  }


  return (
    <div className='p-8 max-w-xl mx-auto'>
      <ul>
        <Folder
          node={parent}
          createAsset={createAsset}
          deleteAsset={deleteAsset}
        />
      </ul>
    </div>
  )
}

// RECUSIVE COMPONENT 
interface FolderProps {
  node: FolderNode
  createAsset: (name: string, parentId: string | null, type: "FOLDER" | "FILE") => FolderNode;
  deleteAsset: (id: string) => void;

}
const Folder = ({ createAsset, deleteAsset, node }: FolderProps) => {
  const { name, id, parentId, children, type, } = node
  // ------------------ STATE ------------------
  const [isOpen, setIsOpen] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [newName, setNewName] = useState(name)

  const hasChildren = children.length > 0

  const handleCreateAsset = () => {
    const fileRegex = /\.[a-zA-Z0-9]+$/;
    const splitedName = newName.trim().split('/')
    // check if the name is emptyq
    if (!newName.trim()) {
      setIsEditing(false)
      return
    }

    if (splitedName.length > 1) {
      // CREATE FOLDER and FILE

      // check is the starting name is a same as parent folder
      const isParentFolderFiles = splitedName[0].trim() === name ? true : false
      console.log(isParentFolderFiles, splitedName, name)

      let parentId = id
      for (let i = isParentFolderFiles ? 1 : 0; i < splitedName.length; i++) {
        const name = splitedName[i].trim()
        if (!name) continue
        const type = fileRegex.test(name) ? "FILE" : "FOLDER"
        const asset = createAsset(name, parentId, type)
        parentId = asset.id // UPDATE PARENT ID

      }
    }
    else {
      const type = fileRegex.test(newName) ? "FILE" : "FOLDER"
      createAsset(newName, id, type)

    }

    setNewName('')
    setIsEditing(false)
  }

  return (
    <li className='my-2'
    >
      <span
        className='flex items-center gap-x-2  cursor-pointer'>

        {/* LABEL */}
        <span
          onClick={() => setIsOpen(!isOpen)}
          className='flex items-center gap-x-2'>
          {
            type === "FOLDER" ? (
              isOpen ? <FcOpenedFolder className='size-6' /> : <FcFolder className='size-6' />
            ) : <FcFile className='size-6' />
          }
          <p className='ml-2'>{name}</p>
        </span>

        {/* ACTIONS */}

        {
          type === "FOLDER" && (

            <div className='flex items-center gap-x-2 ml-4' >
              <button onClick={() => setIsEditing(!isEditing)}>
                <FcPlus className='size-4' />
              </button>
              {
                parentId && (

                  <button onClick={() => deleteAsset(id)}>
                    <FiTrash className='size-4' />
                  </button>
                )}
            </div>
          )
        }
      </span>

      {/* EDITING */}
      {
        isEditing && (
          <div className='flex items-center gap-x-2 mt-2'>
            <input
              type='text'
              value={newName}
              onChange={(e) => setNewName(e.target.value)}
              className='border p-1'
              onKeyPress={(e) => e.key === 'Enter' && handleCreateAsset()}
            />
          </div>
        )
      }

      {hasChildren && isOpen && (
        <ul className='pl-4'>
          {children.map((child) => (
            <Folder key={child.id}
              node={child}
              createAsset={createAsset}
              deleteAsset={deleteAsset}
            />
          ))}
        </ul>
      )}
    </li>
  )


}


export default App
