import { Name } from './roll';

export type Date = {
    year: string | undefined,
    dayMonth: string | undefined,
}

export type Parent = {
    name: string | undefined,
    origin: string | undefined,
}

export type Parents = {
    mother: Parent | undefined,
    father: Parent | undefined,
}

export type Birth = {
    date: Date,
    country: string | undefined,
}

export type Origins = {
    birth: Birth,
    parents: Parents,
    inNzLength: string,
}

export type ArmyExperience = {
    unit: string | undefined,
    country: string | undefined,
    conflict: string | undefined,
    duration: string | undefined,
}

export type Employment = {
    occupation: string | undefined,
    employer: string | undefined,
}

export type PreWayYears = {
    armyExperience: ArmyExperience[] | [],
    employment: Employment
    residence: string | undefined;
    maritalStatus: string | undefined,
    wife: string | undefined,
    religion: string | undefined,
}

export type Transferred = {
    date: Date,
    postedFrom: string,
}

export type Enlistment = {
    serial: string,
    rank: string,
    date: Date,
    district: string | undefined,
    alias: string | undefined,
    transferredToTunnellers: Transferred | undefined,
}

export type Training = {
    date: Date,
    location: string,
    locationType: string,
}

export type EmbarkationUnit = {
    detachment: string,
    training: Training,
    section: string | undefined,
    attachedCorps: string | undefined,
}

export type Transport = {
    reference: string | undefined,
    vessel: string,
    departureDate: Date
    departurePort: string | undefined,
    arrivalDate: Date | undefined,
    arrivalPort: string | undefined,
}

export type DeathPlace = {
    location: string,
    town: string,
    country: string,
}

export type DeathCause = {
    type: string,
    circumstances: string,
}

export type Cemetery = {
    name: string,
    location: string,
    country: string,
    graveReference: string,
}

export type Death = {
    date: Date,
    place: DeathPlace | undefined,
    cause: DeathCause | undefined,
    cemetery: Cemetery | undefined,
}

export type Demobilization = {
    date: Date,
    country: string | undefined,
}

export type EndOfService = {
    deserter: boolean,
    transferred: Transferred | undefined,
    deathWar: Death | undefined,
    transportNz: Transport | undefined,
    demobilization: Demobilization | undefined,
}

export type Medal = {
    name: string,
    country: string,
    citation: string | undefined,
}

export type MilitaryYears = {
    enlistment: Enlistment,
    embarkationUnit: EmbarkationUnit,
    transportUk: Transport,
    endOfService: EndOfService,
    medals: Medal[] | [],
}

export type PostWarDeath = Death & {
    deathWarInjury: boolean,
}

export type PostServiceYears = {
    death: PostWarDeath,
}

export type NzArchives = {
    ibid?: string,
    reference: string,
    url: string,
}

export type Book = {
    title: string,
    town: string,
    publisher: string,
}

export type NominalRoll = Book & {
    date: string,
    page: string,
    volume: string | undefined,
    roll: string | undefined,
}

export type LondonGazette = {
    ibid?: string;
    page: string,
    date: string,
}

export type Sources = {
    nzArchives: NzArchives[],
    awmmCenotaph: string,
    nominalRoll: NominalRoll,
    londonGazette: LondonGazette[] | [],
}

export type ImageArchives = {
    location: string,
    reference: string,
}

export type ImageNewspaper = {
    name: string,
    date: string,
}

export type ImageBookAuthor = {
    forename: string,
    surname: string,
}

export type ImageBook = Book & {
    authors: ImageBookAuthor[],
    year: string,
    page: string | undefined,
}

export type ImageSource = {
    aucklandLibraries: string | undefined,
    archives: ImageArchives | undefined,
    family: string | undefined,
    newspaper: ImageNewspaper | undefined,
    book: ImageBook | undefined,
}

export type Image = {
    url: string,
    source: ImageSource,
}

export type Summary = {
    serial: string,
    name: Name,
    birth: string | undefined,
    death: string | undefined,
}

export type Profile = {
    id: number,
    summary: Summary,
    origins: Origins,
    preWarYears: PreWayYears,
    militaryYears: MilitaryYears,
    postServiceYears: PostServiceYears,
    sources: Sources,
    image: Image | undefined,
}
