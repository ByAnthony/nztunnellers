import { Details } from './roll';

type Date = {
    year: string | undefined,
    dayMonth: string | undefined,
}

type Parent = {
    name: string | undefined,
    origin: string | undefined,
}

type Parents = {
    mother: Parent | undefined,
    father: Parent | undefined,
}

type Birth = {
    date: Date,
    country: string | undefined,
}

type Origins = {
    birth: Birth,
    parents: Parents,
    inNzLength: string,
}

type ArmyExperience = {
    unit: string | undefined,
    country: string | undefined,
    conflict: string | undefined,
    duration: string | undefined,
}

type Employment = {
    occupation: string | undefined,
    employer: string | undefined,
}

type PreWayYears = {
    armyExperience: ArmyExperience[] | [],
    employment: Employment
    residence: string | undefined;
    maritalStatus: string | undefined,
    wife: string | undefined,
    religion: string | undefined,
}

type Transferred = {
    date: Date,
    postedFrom: string,
}

type Enlistment = {
    rank: string,
    date: Date,
    district: string | undefined,
    alias: string | undefined,
    transferredToTunnellers: Transferred | undefined,
}

type Training = {
    date: Date,
    location: string,
    locationType: string,
}

type EmbarkationUnit = {
    training: Training,
    detachment: string,
    section: string | undefined,
    attachedCorps: string | undefined,
}

type Transport = {
    reference: string | undefined,
    vessel: string,
    departureDate: Date
    departurePort: string | undefined,
    arrivalDate: Date | undefined,
    arrivalPort: string | undefined,
}

type DeathPlace = {
    location: string,
    town: string,
    country: string,
}

type DeathCause = {
    type: string,
    circumstances: string,
}

type Cemetery = {
    name: string,
    location: string,
    country: string,
    graveReference: string,
}

type Death = {
    date: Date,
    place: DeathPlace | undefined,
    cause: DeathCause | undefined,
    cemetery: Cemetery | undefined,
}

type Demobilization = {
    date: Date,
    country: string | undefined,
}

type EndOfService = {
    deserter: boolean,
    transferred: Transferred | undefined,
    deathWar: Death | undefined,
    transportNz: Transport | undefined,
    demobilization: Demobilization | undefined,
}

type Medal = {
    name: string,
    country: string,
    citation: string | undefined,
}

type MilitaryYears = {
    enlistment: Enlistment,
    embarkationUnit: EmbarkationUnit,
    transportUk: Transport,
    endOfService: EndOfService,
    medals: Medal[] | [],
}

type PostWarDeath = Death & {
    deathWarInjury: boolean,
}

type PostServiceYears = {
    death: PostWarDeath,
}

type NzArchives = {
    reference: string,
    url: string,
}

type Book = {
    title: string,
    town: string,
    publisher: string,
}

type NominalRoll = Book & {
    date: string,
    page: string,
    volume: string | undefined,
    roll: string | undefined,
}

type LondonGazette = {
    page: string,
    date: string,
}

type Sources = {
    nzArchives: NzArchives[],
    awwmCenotaph: string,
    nominalRoll: NominalRoll,
    londonGazette: LondonGazette[] | [],
}

type ImageArchives = {
    location: string,
    reference: string,
}

type ImageNewspaper = {
    name: string,
    date: string,
}

type ImageBookAuthor = {
    forename: string,
    surname: string,
}

type ImageBook = Book & {
    authors: ImageBookAuthor[],
    year: string,
    page: string | undefined,
}

type ImageSource = {
    aucklandLibraries: string | undefined,
    archives: ImageArchives | undefined,
    family: string | undefined,
    newspaper: ImageNewspaper | undefined,
    book: ImageBook | undefined,
}

type Image = {
    url: string,
    source: ImageSource,
}

export type Profile = Details & {
    origins: Origins,
    preWarYears: PreWayYears,
    militaryYears: MilitaryYears,
    postServiceYears: PostServiceYears,
    sources: Sources,
    image: Image | undefined,
}
