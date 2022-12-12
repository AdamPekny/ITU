export interface Spot {
  id: number,
  name: string,
  latitude: number,
  longitude: number,
  owner: User,
  spotType: string,
  images?: string[],
  likes?: number,
  user?: User,
  description: string,
  spot_type: string
}

export interface Type {
  type_name: string,
  display_name: string
}

export interface User {
  id: number,
  lastLogin: string,
  username: string,
}