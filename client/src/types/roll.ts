export type Name = {
    forename: string;
    surname: string;
}

export type Details = {
    id: number;
    name: Name;
    birth: string | null;
    death: string | null;
}
