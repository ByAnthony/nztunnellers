export const today = new Date();

export const nonNullish = (data: any) => {
  if (data !== null) {
    return true;
  }
  return false;
};
