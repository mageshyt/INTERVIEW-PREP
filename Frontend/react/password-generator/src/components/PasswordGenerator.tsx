import React, { useState } from 'react'

interface passwordCharacteristics {
  length: number;
  includeUppercase: boolean;
  includeLowercase: boolean;
  includeNumbers: boolean;
  includeSymbols: boolean;
}

type passwordStrength = 'weak' | 'medium' | 'strong';
type passwordCharacteristicsType = 'Lowercase' | 'Uppercase' | 'Numbers' | 'Symbols';
const characteristics = [
  { label: 'Include Uppercase', value: 'Uppercase' },
  { label: 'Include Lowercase', value: 'Lowercase' },
  { label: 'Include Numbers', value: 'Numbers' },
  { label: 'Include Symbols', value: 'Symbols' },
];



const PasswordGenerator = () => {
  // ------------------------- STATE -------------------------
  const [password, setPassword] = useState('')
  const [passwordCharacteristics, setPasswordCharacteristics] = useState<passwordCharacteristics>({
    length: 10,
    includeUppercase: false,
    includeLowercase: false,
    includeNumbers: false,
    includeSymbols: false
  })
  const [passwordStrength, setPasswordStrength] = useState<passwordStrength>('weak')

  // ------------------------- PASSWORD GENERATOR ----------------

  const generatePassword = () => {
    let password = ''
    const uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    const lowercase = 'abcdefghijklmnopqrstuvwxyz'
    const numbers = '0123456789'
    const symbols = '!@#$%^&*()_+='

    let characters = ''

    if (passwordCharacteristics.includeUppercase) characters += uppercase
    if (passwordCharacteristics.includeLowercase) characters += lowercase
    if (passwordCharacteristics.includeNumbers) characters += numbers
    if (passwordCharacteristics.includeSymbols) characters += symbols

    for (let i = 0; i < passwordCharacteristics.length; i++) {
      password += characters.charAt(Math.floor(Math.random() * characters.length))
    }

    setPassword(password)
    setPasswordStrength(checkStrength())

  }
  // ------------------------- PASSWORD STRENGTH CHECKER -------------------------

  const checkStrength = (): passwordStrength => {
    const { length, includeUppercase, includeLowercase, includeNumbers, includeSymbols } = passwordCharacteristics;

    let score = 0;
    if (includeUppercase) score += 1;
    if (includeLowercase) score += 1;
    if (includeNumbers) score += 1;
    if (includeSymbols) score += 1;

    if (length < 8) return 'weak';
    if (score >= 3 && length >= 12) return 'strong';
    if (score >= 2 && length >= 10) return 'medium';

    return 'weak';
  };

  // ------------------------- EVENT HANDLERS ----------------


  const handleLengthChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setPasswordCharacteristics((prev) => ({
      ...prev,
      length: parseInt(e.target.value)
    }))

  }

  const handleCharacteristicsChange = (
    e: React.ChangeEvent<HTMLInputElement>,
    characteristic: passwordCharacteristicsType
  ) => {
    const characteristicKey = `include${characteristic}` as keyof passwordCharacteristics;

    setPasswordCharacteristics((prev) => ({
      ...prev,
      [characteristicKey]: e.target.checked
    }))
  }

  // ------------------------- COPY TO CLIPBOARD ----------------

  const handleCopy = () => {

    try {
      if (!password) return

      navigator.clipboard.writeText(password)
    }
    catch (error) {
      console.error('Failed to copy!', error)
    }
  }


  return (
    <div className="bg-neutral-900 flex flex-col justify-between p-4 rounded-md w-[650px] h-fit space-y-4">

      {/* HEADER */}
      <div className="flex justify-between items-center">
        <h1 className="text-white text-2xl font-semibold">{password ? password : "**********"}</h1>
        <button onClick={handleCopy} className="text-white text-sm p-2 rounded-xl duration-200 hover:bg-neutral-700/40 font-semibold">Copy 📋</button>
      </div>

      {/* PASSWORD  CHARACTERISTICS */}
      <div className="">
        {/* LENGTH */}

        <div className='text-left space-y-1'>
          <label className="text-white text-left text-xl font-semibold">Characher Length</label>
          <input type="range" className="w-full" max={25} onChange={handleLengthChange} value={
            passwordCharacteristics.length
          } />
        </div>

        {/* INCLUDES */}

        <div className='flex flex-wrap justify-evenly items-start gap-4'>
          {
            characteristics.map((characteristics,idx)=>(
            <div
              key={idx}
              className="flex items-center space-x-2">
              
              <input
                type="checkbox"
                className="size-4"
                onChange={(e) => handleCharacteristicsChange(e, characteristics.value)}
              />
              <label className="text-white text-xl font-semibold">{characteristics.label}</label>

              </div>
            ))
          }

        </div>


      </div>

      {/* PASSWORD STRENGTH */}
      <div className="flex justify-between items-center">
        <h1 className="text-white text-xl font-semibold">Password Strength</h1>
        <p className="text-white text-xl font-semibold">{passwordStrength}</p>
      </div>

      {/* ACTION BUTTON */}

      <button
        onClick={generatePassword}
        className="p-3 w-full text-black bg-white rounded-xl text-xl font-semibold">
        Generate Password
      </button>
    </div>
  )
}

export default PasswordGenerator

